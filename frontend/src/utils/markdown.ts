import { marked } from 'marked';

export const renderMarkdown = (content: string): string => {
  return marked(content);
};

export const sanitizeMarkdown = (content: string): string => {
  // Basic sanitization - in production, use a library like DOMPurify
  return content.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
};
