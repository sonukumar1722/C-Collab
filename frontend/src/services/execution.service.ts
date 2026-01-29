import api from './api';

export interface ExecutionRequest {
  code: string;
  language: 'c' | 'cpp';
  stdin?: string;
}

export interface ExecutionResult {
  output: string;
  error?: string;
  execution_time: number;
  exit_code: number;
}

export const executionService = {
  executeCode: async (request: ExecutionRequest): Promise<ExecutionResult> => {
    const response = await api.post('/execution/run', request);
    return response.data;
  },

  getExecutionStatus: async (executionId: string) => {
    const response = await api.get(`/execution/${executionId}`);
    return response.data;
  },
};
