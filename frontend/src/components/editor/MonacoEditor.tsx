import React from 'react';

const MonacoEditor: React.FC = () => {
  return (
    <div className="monaco-editor">
      {/* Monaco Editor will be integrated here */}
      <textarea 
        placeholder="Enter your C/C++ code here..."
        style={{ width: '100%', height: '200px' }}
      />
    </div>
  );
};

export default MonacoEditor;
