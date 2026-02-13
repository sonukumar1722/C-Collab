import React from 'react';
import MonacoEditor from '../editor/MonacoEditor';
import Output from './Output';

const CodeCell: React.FC = () => {
  return (
    <div className="code-cell">
      <MonacoEditor />
      <Output />
    </div>
  );
};

export default CodeCell;
