import React from 'react';
import CodeCell from './CodeCell';
import MarkdownCell from './MarkdownCell';

interface CellProps {
  type: 'code' | 'markdown';
}

const Cell: React.FC<CellProps> = ({ type }) => {
  return (
    <div className="cell">
      {type === 'code' ? <CodeCell /> : <MarkdownCell />}
    </div>
  );
};

export default Cell;
