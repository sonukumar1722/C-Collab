import api from './api';

export interface Notebook {
  id: string;
  title: string;
  cells: Cell[];
  created_at: string;
  updated_at: string;
}

export interface Cell {
  id: string;
  type: 'code' | 'markdown';
  content: string;
  output?: string;
}

export const notebookService = {
  getNotebooks: async () => {
    const response = await api.get('/notebooks');
    return response.data;
  },

  getNotebook: async (id: string) => {
    const response = await api.get(`/notebooks/${id}`);
    return response.data;
  },

  createNotebook: async (title: string) => {
    const response = await api.post('/notebooks', { title });
    return response.data;
  },

  updateNotebook: async (id: string, data: Partial<Notebook>) => {
    const response = await api.put(`/notebooks/${id}`, data);
    return response.data;
  },

  deleteNotebook: async (id: string) => {
    const response = await api.delete(`/notebooks/${id}`);
    return response.data;
  },
};
