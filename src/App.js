import './App.css';
import { useState, useEffect } from 'react';
import Table from './Table.js'

const App = () => {
  const [currentTable, setCurrentTable] = useState("/inventory")

  return (
    <div className="App">
      <Table data={currentTable} />
    </div>
  )
}

export default App;
