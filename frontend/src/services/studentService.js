import api from "./api";

export const registerStudent = async (studentData) => {
  const response = await api.post("/students", studentData);
  return response.data;
};