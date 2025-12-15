import Button from './Button.js'

const ButtonList = ({ setCurrentTable, setCurrentName }) => {

    const handleClick = (url, name) => {
        setCurrentTable(url);
        setCurrentName(name);
    }

    return (
        <div>
        <Button 
            url="/products"
            name="Products"
            onClick={handleClick}
        />
        <Button
            url="/suppliers"
            name="Suppliers"
            onClick={handleClick}
        />
        <Button 
            url="/product_suppliers"
            name="Product Suppliers"
            onClick={handleClick}
        />
        <Button 
            url="/sales"
            name="Sales"
            onClick={handleClick}
        />
        <Button 
            url="/inventory"
            name="Inventory"
            onClick={handleClick}
        />
        <Button
            url="/daily_demand"
            name="Daily Demand"
            onClick={handleClick}
        />
        <Button
            url="/future_sales"
            name="Future Sales"
            onClick={handleClick}
        />
        </div>
    )
}

export default ButtonList