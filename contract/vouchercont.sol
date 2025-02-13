// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MarriageCertificate {
    struct Certificate {
        string date;
        string officiant;
        string area;
        string husbandName;
        string husbandNationalID;
        string husbandAgent;
        string wifeName;
        string wifeNationalID;
        string wifeGuardian;
        string witness1Name;
        string witness1NationalID;
        string witness2Name;
        string witness2NationalID;
    }

    Certificate public certificate;

    function setCertificate(
        string memory _date,
        string memory _officiant,
        string memory _area,
        string memory _husbandName,
        string memory _husbandNationalID,
        string memory _husbandAgent,
        string memory _wifeName,
        string memory _wifeNationalID,
        string memory _wifeGuardian,
        string memory _witness1Name,
        string memory _witness1NationalID,
        string memory _witness2Name,
        string memory _witness2NationalID
    ) public {
        certificate = Certificate(
            _date,
            _officiant,
            _area,
            _husbandName,
            _husbandNationalID,
            _husbandAgent,
            _wifeName,
            _wifeNationalID,
            _wifeGuardian,
            _witness1Name,
            _witness1NationalID,
            _witness2Name,
            _witness2NationalID
        );
    }

    function getCertificate() public view returns (Certificate memory) {
        return certificate;
    }
}
