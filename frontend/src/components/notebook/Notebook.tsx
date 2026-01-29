import React from 'react';
import CellList from './CellList';

const Notebook: React.FC = () => {
  return (
    <div className="notebook-container">
      <h1>C/C++ Notebook</h1>
      <CellList />
    </div>
  );
};

export default Notebook;
