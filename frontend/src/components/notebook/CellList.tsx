import React from 'react';
import Cell from './Cell';

const CellList: React.FC = () => {
  return (
    <div className="cell-list">
      <Cell type="code" />
    </div>
  );
};

export default CellList;
