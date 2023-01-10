// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ERC20.sol";

contract Exchange is ERC20 {

    address public cryptoDevContractAddress;

    constructor(address _address) ERC20("CryptoDev LP Token", "CDLP"){
        require(_address!=address(0), "Null Address input not allowed");
        cryptoDevContractAddress=_address;
    }
    
    function getReserves()public view returns(uint){
        return ERC20(cryptoDevContractAddress).balanceOf(address(this));
    
    }
    function addLiquidity(uint _amount)public payable returns(uint){
        uint liquidity;
        uint ethBalance=address(this).balance;
        uint cryptoDevTokenReserve=getReserves();
        ERC20 cryptoDevToken=ERC20(cryptoDevContractAddress);

        if(cryptoDevTokenReserve==0){
            cryptoDevToken.transferFrom(msg.sender, address(this), _amount);
            liquidity=ethBalance;
            _mint(msg.sender, liquidity);

        }
        else{
        uint ethReserve =  ethBalance - msg.value;
        
        uint cryptoDevTokenAmount = (msg.value * cryptoDevTokenReserve)/(ethReserve);
        require(_amount >= cryptoDevTokenAmount, "Amount of tokens sent is less than the minimum tokens required");
        
        cryptoDevToken.transferFrom(msg.sender, address(this), cryptoDevTokenAmount);
        
        liquidity = (totalSupply() * msg.value)/ ethReserve;
        _mint(msg.sender, liquidity);
    }
     return liquidity;
    }
    function removeLiquidity(uint _amount) public returns (uint , uint) {
    require(_amount > 0, "_amount should be greater than zero");
    uint ethReserve = address(this).balance;
    uint _totalSupply = totalSupply();
    
    uint ethAmount = (ethReserve * _amount)/ _totalSupply;
    
    uint cryptoDevTokenAmount = (getReserves() * _amount)/ _totalSupply;
    
    _burn(msg.sender, _amount);
    
    payable(msg.sender).transfer(ethAmount);
    ERC20(cryptoDevContractAddress).transfer(msg.sender, cryptoDevTokenAmount);
    return (ethAmount, cryptoDevTokenAmount);
}
function getAmountOfTokens(
        uint256 inputAmount,
        uint256 inputReserve,
        uint256 outputReserve
    ) public pure returns (uint256) {
        require(inputReserve > 0 && outputReserve > 0, "invalid reserves");
        
        uint256 inputAmountWithFee = inputAmount * 99;
        
        uint256 numerator = inputAmountWithFee * outputReserve;
        uint256 denominator = (inputReserve * 100) + inputAmountWithFee;
        return numerator / denominator;
    }

    
    function ethToCryptoDevToken(uint _minTokens) public payable {
        uint256 tokenReserve = getReserves();
        
        uint256 tokensBought = getAmountOfTokens(
            msg.value,
            address(this).balance - msg.value,
            tokenReserve
        );

        require(tokensBought >= _minTokens, "insufficient output amount");
        
        ERC20(cryptoDevContractAddress).transfer(msg.sender, tokensBought);
    }


    
    function cryptoDevTokenToEth(uint _tokensSold, uint _minEth) public {
        uint256 tokenReserve = getReserves();
        
        uint256 ethBought = getAmountOfTokens(
            _tokensSold,
            tokenReserve,
            address(this).balance
        );
        require(ethBought >= _minEth, "insufficient output amount");
        
        ERC20(cryptoDevContractAddress).transferFrom(
            msg.sender,
            address(this),
            _tokensSold
        );
        
        payable(msg.sender).transfer(ethBought);
    }
    



}
