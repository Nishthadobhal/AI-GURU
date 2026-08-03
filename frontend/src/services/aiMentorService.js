import axios from "axios";

const API = "http://127.0.0.1:8000";

export const askAIMentor = async (studentId, question) => {

    const response = await axios.post(

        `${API}/ai-mentor`,

        {
            student_id: studentId,
            question: question
        }

    );

    return response.data;

};