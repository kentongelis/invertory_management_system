# Inventory Management System

A full-stack inventory management application with natural language database querying powered by LangChain and OpenAI.

## Overview

This system provides a comprehensive inventory management solution with the following features:

- **Product Management**: Track products, suppliers, and inventory levels
- **Sales Analytics**: Monitor sales transactions and daily demand patterns
- **Natural Language Queries**: Ask questions about your data in plain English using AI-powered SQL generation
- **Real-time Data Visualization**: View and filter data through interactive tables

## Tech Stack

### Backend
- **Flask**: Python web framework
- **SQLAlchemy**: ORM for database management
- **SQLite**: Database engine
- **LangChain**: AI-powered query generation
- **OpenAI GPT-4**: Natural language processing
- **Marshmallow**: Data serialization

### Frontend
- **React**: UI framework
- **react-data-table-component**: Interactive data tables

## Database Schema

The system includes six main tables:

1. **products** - Product catalog with SKUs, pricing, and specifications
2. **suppliers** - Supplier contact information
3. **product_suppliers** - Product-supplier relationships with lead times
4. **sales** - Complete transaction history
5. **inventory** - Current stock levels and reorder points
6. **daily_demand** - Aggregated daily demand for forecasting

## Project Structure

```
├── backend/
│   ├── langchain/
│   │   ├── .env                    # OpenAI API key
│   │   ├── langchain.py            # LangChain SQL agent
│   │   └── database_table_descriptions.csv
│   ├── models/
│   │   └── data_models.py          # SQLAlchemy models
│   ├── routes/
│   │   └── main.py                 # Flask API routes
│   ├── schemas/
│   │   └── schemas.py              # Marshmallow schemas
│   ├── scripts/
│   │   ├── generate_inventory_data.py  # Data generator
│   │   └── jsonintodb.py           # Database seeder
│   └── server/
│       ├── app.py                  # Flask application
│       ├── config.py               # Configuration
│       ├── extensions.py           # Flask extensions
│       └── inventory.db            # SQLite database
├── src/
│   ├── App.js                      # Main React component
│   ├── Table.js                    # Data table component
│   ├── ButtonList.js               # Navigation buttons
│   ├── Button.js                   # Button component
│   └── SQLSearch.js                # Natural language search
└── README.md
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 14+
- OpenAI API key

### Backend Setup

1. **Install Python dependencies**:
```bash
cd backend/server
pip install -r requirements.txt
```

2. **Configure environment variables**:
   
   Create or update `backend/langchain/.env`:
```
OPENAI_API_KEY=your_openai_api_key_here
```

   Update `backend/server/.env` if needed:
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
```

3. **Generate sample data** (optional):
```bash
cd backend/scripts
python generate_inventory_data.py
```

4. **Seed the database**:
```bash
python jsonintodb.py
```

5. **Run the Flask server**:
```bash
cd backend/server
flask run
```

The backend will be available at `http://localhost:5000`

### Frontend Setup

1. **Install Node dependencies**:
```bash
npm install
```

2. **Start the React development server**:
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## Usage

### Viewing Data
- Use the navigation buttons to switch between different tables (Products, Suppliers, Sales, etc.)
- Use the search box to filter table data in real-time
- Click column headers to sort data

### Natural Language Queries
The AI-powered search feature allows you to ask questions in plain English:

**Example queries**:
- "What is the current stock of Wireless Mouse?"
- "Show me all products with low inventory status"
- "What are the total sales for each product?"
- "Which products cost more than $100?"
- "List suppliers for Electronics category"

The system will:
1. Convert your question to SQL
2. Execute the query
3. Return a natural language answer

## API Endpoints

- `GET /products` - Retrieve all products
- `GET /suppliers` - Retrieve all suppliers
- `GET /product_suppliers` - Retrieve product-supplier relationships
- `GET /sales` - Retrieve sales transactions
- `GET /inventory` - Retrieve inventory levels
- `GET /daily_demand` - Retrieve daily demand data
- `POST /ask_db` - Submit natural language queries

## Data Generation

The included data generator (`generate_inventory_data.py`) creates realistic sample data including:

- 28 products across 5 categories (Electronics, Office Supplies, Furniture, Software, Maintenance)
- 5 suppliers with contact information
- 2 years of historical sales data with seasonal trends
- Current inventory levels based on sales patterns
- Daily demand summaries for forecasting

## LangChain Integration

The system uses LangChain to:
- Parse natural language questions
- Generate appropriate SQL queries with JOINs when needed
- Execute queries against the SQLite database
- Format results into natural language responses

The LangChain agent understands:
- Table relationships and foreign keys
- Common business terminology
- Multi-table queries requiring JOINs
- Context about inventory, pricing, and stock levels

## Security Notes

⚠️ **Important**: The `.env` files in this repository contain API keys for demonstration purposes. In a production environment:

- Never commit API keys to version control
- Use environment variables or secure secret management
- Add `.env` files to `.gitignore`
- Rotate exposed keys immediately

## Future Enhancements

Potential improvements:
- User authentication and authorization
- Real-time inventory updates
- Automated reordering system
- Advanced analytics and forecasting
- Export functionality (CSV, PDF)
- Mobile responsive design
- Dashboard with visualizations
- Multi-warehouse support

## License

This project is for educational purposes.

## Support

For issues or questions, please refer to the documentation or create an issue in the repository.