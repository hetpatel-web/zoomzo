const React = require('react');

function HomePage() {
  return React.createElement(
    'div',
    null,
    React.createElement('h1', null, 'Welcome to Zoomzo'),
    React.createElement('p', null, 'Get started by editing the page')
  );
}

module.exports = HomePage;
