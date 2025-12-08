import { useState, useEffect } from 'react';
import DataTable from 'react-data-table-component';

const Table = ({ data, name }) => {
  const [records, setRecords] = useState([]);
  const [baseData, setBaseData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(data)
      .then((res) => res.json())
      .then((data) => {
        setRecords(data);
        setBaseData(data);
      })
      .catch((err) => {
        console.error(err);
        setError('Failed to load data');
      });
  }, [data]);

  const buildColumns = (rows) => {
    if (!rows || rows.length === 0) return [];

    return Object.keys(rows[0]).map(key => ({
      name: key.charAt(0) + key.slice(1),
      selector: row => row[key],
      sortable: true,
    }));
  };

  const columns = buildColumns(records);

  const handleFilter = (event) => {
    const searchValue = event.target.value.toLowerCase();

    const newData = baseData.filter(row => 
      Object.values(row).some(value => 
        String(value).toLowerCase().includes(searchValue)
      )
    );

    setRecords(newData);
  };

  return (
    <div className="App">
      <h1>{name}</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div><input type='text' placeholder="Search..." onChange={handleFilter} /></div>
      <DataTable 
        columns={columns}
        data={records}
        fixedHeader
        pagination
      />
    </div>
  );
};

export default Table;
