// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;


struct Data{
    string  newOwner;
    string  prevOwner;
    string  regPrice;
    string  landId;
    string aadharPrevOwner;
    string aadharNewOwner;
    uint timestamp;
    string oldCoordinates;
    string landCoordinates;

}

contract Registeration{
    Data NewDetails;
function  setDetails(string memory CurrentOwner ,string memory Buyer , string memory Price , string memory LandId,string memory aadharCurrOwner,string memory aadharBuyer,string memory OldLandCoord,string memory NewLandCoord  ) public {

    NewDetails.newOwner  = Buyer;
    NewDetails.prevOwner = CurrentOwner;
    NewDetails.regPrice = Price;
    NewDetails.landId = LandId;
    NewDetails.aadharPrevOwner = aadharCurrOwner;
    NewDetails.aadharNewOwner = aadharBuyer;
    NewDetails.timestamp = block.timestamp;
    NewDetails.oldCoordinates = OldLandCoord;
    NewDetails.landCoordinates = NewLandCoord;
}

function getCurrentOwner() public view returns(string memory ){
    return (NewDetails.newOwner);
}
function setCurrentOwner(string memory _input) public {
    NewDetails.newOwner = _input;
}
function getPreviousOwner() public view returns(string memory ){
    return (NewDetails.prevOwner);
}
function getDetails() public view returns(string memory,string memory ,string memory ,string memory ,string memory ,string memory ,string memory ,string memory,uint ){
    return (NewDetails.newOwner,
    NewDetails.prevOwner,
    NewDetails.regPrice,
    NewDetails.landId,
    NewDetails.aadharPrevOwner,
    NewDetails.aadharNewOwner,
    NewDetails.oldCoordinates,
    NewDetails.landCoordinates,
    NewDetails.timestamp);
}

}