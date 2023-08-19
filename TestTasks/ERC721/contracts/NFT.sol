// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "../node_modules/@openzeppelin/contracts/token/ERC721/extensions/IERC721Enumerable.sol";


contract Token is ERC721 {
    uint256 private initialSupply;
    uint256 private currentId;

    uint256 public mintFee;
    address public feeReceiver;

    constructor(uint256 _initSupply, uint256 _fee) ERC721("Token", "NFT") {
        initialSupply = _initSupply;
        currentId = 0;
        mintFee = _fee;
        feeReceiver = msg.sender;
    }

    function generateId() public returns (uint256) {
        currentId++;
        return currentId;
    }

    function mint(address to, uint256 amountIn) public payable{
        require(to != address(0), "ERC721: mint to the zero address");
        require(amountIn <= 3, "ERC721: mint limit reached!");
        require(balanceOf(to) <= 6, "ERC721: address could own less then 6 tokens!");
        // require(totalSupply() <= initialSupply, "ERC721: address could own less then 6 tokens!");
        
        require(msg.value >= mintFee, "Insufficient fee amount");
        

        address payable tokenReceiver = payable(to);
        address payable feeReceiverPayable = payable(feeReceiver);

        for(uint256 i= 0; i < amountIn; i++ ){
            tokenReceiver.transfer(mintFee); 

            _mint(to, generateId());
            
            feeReceiverPayable.transfer(mintFee); // Transfer the fee to the fee receiver

        }
    }

}