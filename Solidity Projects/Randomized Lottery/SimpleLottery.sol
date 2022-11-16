// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "./random.sol";

contract simpleLottery is RandomNumberConsumer{

address public owner;
address[] public lotteryMembers;
uint public priceOfTicket;
uint public pool;
uint public numberOfPlayers;
uint public startTime;
uint public currentTime= block.timestamp;


constructor (){
    owner=msg.sender;
    priceOfTicket= 100000000000;
    startTime= block.timestamp;
}

modifier isOwner{
    require(msg.sender== owner, "You are not the Owner");
    _;
}

modifier isTime{
    require(block.timestamp>=startTime+15552000, "It isn't time yet");
    _;
}

function setTicketPrice(uint _amount)public isOwner{
    priceOfTicket=_amount;
}

function addToPool() public payable{
    require(msg.value== priceOfTicket, "Not correct ticket price");
    pool +=priceOfTicket;
    numberOfPlayers++;
    lotteryMembers.push(msg.sender);
}


function findWinner() public payable returns(uint){
    getRandomNumber();
    uint blockTime;
    blockTime=block.timestamp;
    if(block.timestamp>=blockTime+300){
    while(randomResult>numberOfPlayers){
        randomResult=(randomResult/2)+1;
    }
    return randomResult;
    }
}

function sendFunds() public payable isTime returns(string memory) {
    address winner= lotteryMembers[findWinner()];
    address payable winnerCasted= payable(winner);
    winnerCasted.transfer(pool);
    delete lotteryMembers;
    pool=0;
    numberOfPlayers=0;
    startTime=block.timestamp;
    return "Funds sent to winner. Lottery has been reset.";
}



}