import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';


//const endpoint = "https://udbank-backend.herokuapp.com/api/v1/user/";
const endpoint = "http://localhost:3000/api/v1/user/";

@Injectable({
  providedIn: 'root'
})
export class AuthorizationService {
  headers: HttpHeaders;

  constructor(private http: HttpClient) {
    this.headers = new HttpHeaders();
   }


  login(body: any): Promise<any> {
    return this.http.post(`${endpoint}login`,body, {headers: this.headers}).toPromise();
  }

  register(body: any): Promise<any> {
    return this.http.post(`${endpoint}register`, body, { headers: this.headers }).toPromise();
  }

  logout(): Promise<any> {
    return this.http.delete(`${endpoint}logout`, {headers: this.headers}).toPromise();
  }

  update(body: any): Promise<any> {
    return this.http.post(`${endpoint}info`, body, {headers: this.headers}).toPromise();
  }

  description(): Promise<any> {
    return this.http.get(`${endpoint}info`, {headers: this.headers}).toPromise();
  }

}
