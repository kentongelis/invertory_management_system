import { useState, useEffect } from 'react';

const Table = ({data}) =>  {
      const [products, setProducts] = useState([]);
      const [error, setError] = useState(null);
    
      useEffect(() => {
        fetch(data)
          .then((res) => res.json())
          .then((data) => {
            console.log(data);
            setProducts(data);
          })
          .catch((err) => {
            console.error(err);
            setError('Failed to load data');
          });
      }, [data]);
    
      return (
        <div className="App">
          <h1>Data</h1>
    
          {error && <p style={{ color: 'red' }}>{error}</p>}
    
          <ul>
            {products.map((p) => (
              <li>
                {p.id}
              </li>
            ))}
          </ul>
        </div>
      )
}

export default Table