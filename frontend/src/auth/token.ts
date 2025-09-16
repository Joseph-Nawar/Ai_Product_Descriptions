// frontend/src/auth/token.ts
let _token: string | null = null;
export const setIdToken = (t: string | null) => { _token = t; };
export const getIdToken = async () => _token;
