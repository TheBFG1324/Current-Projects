// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ERC20.sol";
import "./Ownable.sol";
import "./ICryptoDevs.sol";

contract CryptoDevToken is ERC20, Ownable{
    uint256 public constant tokenPrice= 0.001 ether;

    uint256 public constant tokensPerNFT=10*10**18;

    uint256 public constant maxTotalSupply=1000*10**18;
    
    ICryptoDevs CryptoDevsNFT;

    mapping(uint256=>bool)public tokenIdsClaimed;

    constructor(address _cryptodevscontract) ERC20("Crypto Dev Token", "CD"){
        CryptoDevsNFT=ICryptoDevs(_cryptodevscontract);
    }

    function mint(uint256 _amount)public payable{
        uint256 _requiredAmount= tokenPrice * _amount;
        require(msg.value>=_requiredAmount, "Ether sent is incorrect");
        uint256 amountWithDecimal=_amount*10**18;
        require((totalSupply()+amountWithDecimal<=maxTotalSupply), "Exceeds the max total supply");
        _mint(msg.sender, amountWithDecimal);
    }
    function claim()public{
        address sender= msg.sender;
        uint256 balance =CryptoDevsNFT.balanceOf(sender);
        require(balance>0, "You dont own any CryptoNFT");
        uint256 amount=0;
        for(uint256 i=0; i<balance;i++){
            uint256 tokenId=CryptoDevsNFT.tokenOfOwnerByIndex(sender, i);
            if(!tokenIdsClaimed[tokenId]){
                amount+=1;
                tokenIdsClaimed[tokenId]=true;
            }
        }
        require(amount>0, "You have already claimed all tokens");
        _mint(sender, amount*tokensPerNFT);
    }

    function withdraw()public onlyOwner{
        uint256 amount= address(this).balance;
        require(amount > 0, "Nothing to withdraw, contract balance empty");
        
        address _owner = owner();
        (bool sent, ) = _owner.call{value: amount}("");
        require(sent, "Failed to send Ether");
      
    }
    receive() external payable{}

    fallback() external payable{}



}