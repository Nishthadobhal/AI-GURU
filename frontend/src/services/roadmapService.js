import api from "./api";

export const generateRoadmap = async (studentId, goal) => {

    const response = await api.post("/ai-roadmap", {
        student_id: studentId,
        goal: goal
    });

    return response.data;
};


// ----------------------------
// Get Saved Roadmap
// ----------------------------

export const getRoadmap = async (studentId) => {

    const response = await api.get(
        `/roadmaps/student/${studentId}`
    );

    return response.data;

};