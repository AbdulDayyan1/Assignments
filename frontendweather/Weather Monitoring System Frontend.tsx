import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const WeatherMonitoringSystem = () => {
  const [weatherData, setWeatherData] = useState([]);
  const [dailySummary, setDailySummary] = useState({});

  useEffect(() => {
    const fetchWeatherData = async () => {
      const response = await fetch('/api/weather');
      const data = await response.json();
      setWeatherData(data);
    };

    const fetchDailySummary = async () => {
      const response = await fetch('/api/daily_summary');
      const data = await response.json();
      setDailySummary(data);
    };

    fetchWeatherData();
    fetchDailySummary();
  }, []);

  const chartData = weatherData.map(data => ({
    city: data.city,
    temp: data.temp,
    dt: new Date(data.dt * 1000).toLocaleString()
  }));

  return (
    <div>
      <h1>Weather Monitoring System</h1>
      <h2>Daily Weather Summary</h2>
      <p>Average Temperature: {dailySummary.average_temp?.toFixed(2)} °C</p>
      <p>Maximum Temperature: {dailySummary.max_temp?.toFixed(2)} °C</p>
      <p>Minimum Temperature: {dailySummary.min_temp?.toFixed(2)} °C</p>
      <p>Dominant Weather Condition: {dailySummary.dominant_weather}</p>

      <h2>Weather Data Visualization</h2>
      <LineChart width={800} height={400} data={chartData}>
        <XAxis dataKey="dt" />
        <YAxis />
        <CartesianGrid strokeDasharray="3 3" />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="temp" stroke="#8884d8" />
      </LineChart>
    </div>
  );
};

export default WeatherMonitoringSystem;
