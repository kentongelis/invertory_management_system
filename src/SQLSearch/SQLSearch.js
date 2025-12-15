import './SQLSearch.css'
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
    <div className="sql-search-container">
      <form className="sql-search-form" onSubmit={handleSubmit}>
        <label className="sql-search-label">
          Question
        </label>
        <input
          id="question"
          type="text"
          className="sql-search-input"
          value={question}
          onChange={handleQuestionChange}
          placeholder="Ask your question here"
        />
        <button
          type="submit"
          className="sql-submit-button"
        >
          Submit
        </button>
      </form>
      {error && <p className="sql-error">{error}</p>}
      {result && <p className="sql-result"><strong>Result:</strong> {result}</p>}
    </div>
    )
}

export default SQLSearch