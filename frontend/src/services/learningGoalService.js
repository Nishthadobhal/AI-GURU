import api from "./api";

export const createLearningGoal = async (goalData) => {

    const response = await api.post(
        "/learning-goals",
        goalData
    );

    return response.data;

};