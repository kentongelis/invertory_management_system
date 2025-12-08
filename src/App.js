import './App.css';
import { useState } from 'react';
import Table from './Table.js'
import ButtonList from './ButtonList.js'

const App = () => {
  const [currentTable, setCurrentTable] = useState("/products")
  const [currentName, setCurrentName] = useState("Products")


  return (
    <div className="App">
      <ButtonList
        setCurrentTable={setCurrentTable}
        setCurrentName={setCurrentName}
      />
      <Table data={currentTable} name={currentName} />
    </div>
  )
}

export default App;
