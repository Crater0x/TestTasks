 // SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
     
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Token is ERC20,  Ownable{
    uint256 public maxTotalSupply;
   
    constructor(uint256 _initSupply, uint256 _amountIn, address[] memory _to) ERC20("TestToken", "TTK") {
        maxTotalSupply = _initSupply;
        for (uint256 i = 0; i < _to.length; i++) {
            _mint(_to[i], _amountIn);
        }
        
    }


    function mint(address to, uint256 amountIn) public onlyOwner() {
        require(totalSupply() + amountIn <= maxTotalSupply, "Token: max Total supply reached!");
        mint(to, amountIn);
    }

    
    function burn(address to, uint256 amount) public onlyOwner(){
        if (balanceOf(to) <= amount) 
            _burn(to, balanceOf(to));
        else
            _burn(to, amount);
        
    }
}