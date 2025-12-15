import "./Button.css"

const Button = ({url, name, onClick}) => {
    return (
        <div>
        <button
            className="table-button"
            onClick={() => onClick(url, name)}
        >
            {name}
        </button>
        </div>
    )
}

export default Button