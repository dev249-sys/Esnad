// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract UserStorage {
    struct User {
        string username;
        string email;
        string passwordHash;
    }

    User[] public users;

    function addUser(string memory _username, string memory _email, string memory _passwordHash) public {
        users.push(User(_username, _email, _passwordHash));
    }

    function getUser(uint _index) public view returns (string memory, string memory, string memory) {
        require(_index < users.length, "Index out of range");
        User memory user = users[_index];
        return (user.username, user.email, user.passwordHash);
    }
}
