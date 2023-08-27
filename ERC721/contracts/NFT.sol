// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Token is ERC721, Ownable {
    using Strings for uint256;

    uint private _maxTotalSupply;
    uint private _mintFee = 0.001 ether;
    address payable private _feeReceiver;

    uint public currentId;
    string public baseTokenURI = "https://black-legal-turkey-600.mypinata.cloud/ipfs/QmSnKuFFxDFiHuTMaoqBHCLPdnM6NFLy2PzgxqG5fN25Bj/";

    constructor(uint _initSupply) ERC721("Token", "NFT") {   
        _maxTotalSupply = _initSupply;
        _feeReceiver = payable(msg.sender);
    }

    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "Token: invalid token ID");

        string memory baseURI = _baseURI();
        return bytes(baseURI).length > 0 ? string(abi.encodePacked(baseURI, tokenId.toString(), ".json")) : "";
    }

    function mint(uint _amountIn) external payable{
        address payable receiver = payable(msg.sender);
        require(_amountIn <= 3, "Token: NFT mint limit reached!");
        require(balanceOf(receiver) + _amountIn <= 6, "Token: address could own less then 6 tokens!");
        require(currentId + _amountIn <= _maxTotalSupply, "Token: max token amount reached!");
        require(msg.value >= _mintFee * _amountIn, "Token: Insufficient fee amount");
        
        for(uint i = 0; i < _amountIn; i++ ){
            (bool success, ) = _feeReceiver.call{value: _mintFee}("");
            require(success, "Failed to send Ether");

            _mint(receiver, currentId);
            currentId++;
        }
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return baseTokenURI;
    }

    function setBaseTokenURI(string memory _baseTokenURI) external {
        baseTokenURI = _baseTokenURI;
    }

}