// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";
// import "../node_modules/@openzeppelin/contracts/token/ERC721/extensions/IERC721Enumerable.sol";


contract Token is ERC721 {
    uint private initialSupply;
    uint private currentId;
    uint private count;

    // uint public mintFee = 0.001 ether;
    uint public mintFee = 1 ether;
    address payable public feeReceiver;

    constructor(uint _initSupply) ERC721("Token", "NFT") {
        initialSupply = _initSupply;
        currentId = 0;
        count = 0;
        feeReceiver = payable(msg.sender);
    }

    function generateId() public returns (uint) {
        return currentId++;
    }

    function mint(uint _amountIn) external payable{
        address payable receiver = payable(msg.sender);
        require(receiver != address(0), "ERC721: mint receiver the zero address");
        require(_amountIn <= 3, "ERC721: mint limit reached!");
        require(balanceOf(receiver) <= 6, "ERC721: address could own less then 6 tokens!");
        require(count + _amountIn <= initialSupply, "ERC721: max token amount reached!");
        require(msg.value >= mintFee * _amountIn, "Insufficient fee amount");
        
        

        

        for(uint i = 0; i < _amountIn; i++ ){
            (bool success, ) = feeReceiver.call{value: mintFee}("");
            require(success, "Failed to send Ether");
            // feeReceiver.transfer(mintFee);

            _mint(receiver, generateId());

            count++;
        }


    }

    function getBalance(address _address) public view returns (uint) {
        return _address.balance;
    }
}