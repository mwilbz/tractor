import React, { Component } from 'react';
import openSocket from "socket.io-client";
import './App.css';
import Button from 'react-bootstrap/button';


const socket = openSocket('ws://localhost:5000');


const joinGame = (gameId) => {
  socket.emit('join_game', gameId, (data) => {

  });
}


const handleClick = () => {
  console.log('Creating game!');
  socket.emit('create_game', (data) => {
    console.log(`Received create_game data ${data}`);
    joinGame(data['game_id'])
  });
}


class App extends Component {
  componentDidMount() {
    socket.on('connect', () => {
      console.log('WebSocket Client Connected');
    });
  }
  
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Tractor? Do you even know 'er?</h2>
        </div>
        <div>
          <Button 
            variant="primary"
            onClick={handleClick}
          >
            Create Game
          </Button>
        </div>
      </div>
    );
  }
}

export default App;