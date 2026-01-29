import { create } from 'zustand';
import { Notebook } from '../services/notebook.service';

interface NotebookState {
  notebooks: Notebook[];
  currentNotebook: Notebook | null;
  setNotebooks: (notebooks: Notebook[]) => void;
  setCurrentNotebook: (notebook: Notebook | null) => void;
  addNotebook: (notebook: Notebook) => void;
  updateNotebook: (id: string, data: Partial<Notebook>) => void;
  deleteNotebook: (id: string) => void;
}

export const useNotebookStore = create<NotebookState>((set) => ({
  notebooks: [],
  currentNotebook: null,
  setNotebooks: (notebooks) => set({ notebooks }),
  setCurrentNotebook: (notebook) => set({ currentNotebook: notebook }),
  addNotebook: (notebook) =>
    set((state) => ({ notebooks: [...state.notebooks, notebook] })),
  updateNotebook: (id, data) =>
    set((state) => ({
      notebooks: state.notebooks.map((n) =>
        n.id === id ? { ...n, ...data } : n
      ),
    })),
  deleteNotebook: (id) =>
    set((state) => ({
      notebooks: state.notebooks.filter((n) => n.id !== id),
    })),
}));
