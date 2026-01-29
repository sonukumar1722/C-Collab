import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Notebook from '../components/notebook/Notebook';

const AppRoutes: React.FC = () => {
  return (
    <Routes>
      <Route path="/" element={<Notebook />} />
      <Route path="/notebook/:id" element={<Notebook />} />
    </Routes>
  );
};

export default AppRoutes;
