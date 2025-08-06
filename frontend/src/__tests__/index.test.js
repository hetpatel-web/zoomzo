const React = require('react');
const { render, screen } = require('@testing-library/react');
require('@testing-library/jest-dom');
const HomePage = require('../index');

describe('HomePage', () => {
  test('renders heading and paragraph', () => {
    render(React.createElement(HomePage));
    expect(
      screen.getByRole('heading', { name: /welcome to zoomzo/i })
    ).toBeInTheDocument();
    expect(
      screen.getByText(/get started by editing the page/i)
    ).toBeInTheDocument();
  });
});
