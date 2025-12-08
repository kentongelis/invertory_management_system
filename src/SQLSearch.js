import { useState } from 'react';

const SQLSearch = () => {

    const [result, setResult] = useState("")
    const [question, setQuestion] = useState("")
    const [error, setError] = useState(null);

    const handleQuestionChange = (event) => {
        setQuestion(event.target.value)
    }

    const handleSubmit = (event) => {
        event.preventDefault()

        const formData = new FormData()

        if (question) {
            formData.append('question', question)
        }

        fetch("/ask_db", {
            method: "POST",
            body: formData
        })
        .then((response) => response.json())
        .then((data) => {
            setResult(data.result)
        })
        .catch((error) => {
            console.error("Error", error)
            setError("An error occurred while fetching data.")
        })
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Question
                </label>
                <input
                    id="question"
                    type="text"
                    value={question}
                    onChange={handleQuestionChange}
                    placeholder="Ask your question here"
                >
                </input>
                <button
                    type="submit"
                >
                    Submit
                </button>
            </form>
            {error && <p style={{ color: "red" }}>{error}</p>}
            {result && <p>Result: {result}</p>}
        </div>
    )
}

export default SQLSearch