import './App.css';
import { useState } from 'react';
import Table from '../Table/Table.js'
import ButtonList from '../ButtonList/ButtonList.js'
import SQLSearch from '../SQLSearch/SQLSearch.js';

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
      <SQLSearch />
    </div>
  )
}

export default App;
