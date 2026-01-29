import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import Routes from './routes';
import '../styles/global.css';

const App: React.FC = () => {
  return (
    <Router>
      <div className="app">
        <Routes />
      </div>
    </Router>
  );
};

export default App;
