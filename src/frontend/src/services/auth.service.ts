import axios from 'axios';

import type { LoginInfo } from '@/types/user';
import authHeader from '@/services/auth-header';

class AuthService {
    getAccessToken(): string {
        return localStorage.getItem('access_token') || '';
    }

    async login(user: LoginInfo) {
        const loginData = new URLSearchParams();
        loginData.append('grant_type', 'password');
        loginData.append('username', user.username);
        loginData.append('password', user.password);

        const response = await axios.post('/api/v1/token/new', loginData);
        this.setAccessToken(response.data.access_token);
        return response.data;
    }

    logout() {
        localStorage.removeItem('access_token');
    }

    async me() {
        const response = await axios.get('/api/v1/user/me', {
            headers: authHeader(),
        });
        return response.data;
    }

    async register(user: LoginInfo) {
        const response = await axios.post('/api/v1/user/register', user);
        return response.data;
    }

    setAccessToken(token: string) {
        localStorage.setItem('access_token', token);
    }
}

export default new AuthService();
