const Button = ({url, name, onClick}) => {
    return (
        <div>
        <button
            onClick={() => onClick(url, name)}
        >
            {name}
        </button>
        </div>
    )
}

export default Button