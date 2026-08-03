import axios from "axios";

const API = "http://127.0.0.1:8000";

export const getStudentReport = async (studentId) => {

    const response = await axios.get(

        `${API}/students/${studentId}/report`

    );

    return response.data;

};