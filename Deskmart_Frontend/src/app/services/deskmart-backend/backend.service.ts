import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

const endpoint = "http://localhost:3000/api/v1/";

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  headers: HttpHeaders;

  constructor(private http: HttpClient) { 
    this.headers = new HttpHeaders();
  }

  get_weather(): Promise<any> {
    return this.http.get(`${endpoint}weather/today`, {headers: this.headers}).toPromise();
  }

  
}
