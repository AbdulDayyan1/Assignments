import React from 'react';
import ReactDOM from 'react-dom';
import WeatherMonitoringSystem from './WeatherMonitoringSystem';

const App = () => {
  return (
    <div>
      <WeatherMonitoringSystem />
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
