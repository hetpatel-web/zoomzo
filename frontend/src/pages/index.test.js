import { render, screen } from '@testing-library/react';
import Home from './index';
import '@testing-library/jest-dom';

describe('Home page', () => {
  it('renders a Deploy now link', () => {
    render(<Home />);
    expect(screen.getByText(/Deploy now/i)).toBeInTheDocument();
  });
});
