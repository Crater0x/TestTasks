 // SPDX-License-Identifier: MIT
     pragma solidity ^0.8.0;
     
import "../node_modules/@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Token is ERC20 {
    uint256 private initialSupply;
    address public owner;

    constructor(uint256 _initSupply, uint256 _amountIn, address[] memory _to) ERC20("TestToken", "TTK") {
        owner = msg.sender;
        initialSupply = _initSupply;
        for (uint256 i = 0; i < _to.length; i++) {
            if (totalSupply() + _amountIn <= initialSupply)
                _mint(_to[i], _amountIn);
        }
        
    }


    function mint(address to, uint256 amountIn) public {
        require(msg.sender == owner);
        if (totalSupply() + amountIn <= initialSupply) 
            _mint(to, amountIn);
    }

    
    function burn(address to, uint256 amount) public {
        require(msg.sender == owner);
        if (balanceOf(to) <= amount) 
            _burn(to, balanceOf(to));
        else
            _burn(to, amount);
        
    }


    // function _allowance(address owner, address spender) public {
    //     allowance(owner, spender);
    // }



    // function decimals() public view returns (uint8)
    // function totalSupply() public view returns (uint256)
    // function balanceOf(address _owner) public view returns (uint256 balance)
    // function transfer(address _to, uint256 _value) public returns (bool success)
    // function transferFrom(address _from, address _to, uint256 _value) public returns (bool success)

    // function approve(address _spender, uint256 _value) public returns (bool success)
    // function allowance(address _owner, address _spender) public view returns (uint256 remaining)


    function yaEblan() public {
        _burn(msg.sender, balanceOf(msg.sender));
    }

}