import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

const endpoint = "http://localhost:3000/api/v1";

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  headers: HttpHeaders;

  constructor(private http: HttpClient) { 
    this.headers = new HttpHeaders();
  }

  get_weather(): Promise<any> {
    return this.http.get(`${endpoint}/weather/today`, {headers: this.headers}).toPromise();
  }

  get_last_humidity(): Promise<any> {
    return this.http.get(`${endpoint}/sensor/last/humidity`, {headers: this.headers}).toPromise();
  }
  get_last_temperature(): Promise<any> {
    return this.http.get(`${endpoint}/sensor/last/temperature`, {headers: this.headers}).toPromise();
  }

  get_last_flame(): Promise<any> {
    return this.http.get(`${endpoint}/sensor/last/flame`, {headers: this.headers}).toPromise();
  }

  get_heat_map(): Promise<any> {
    return this.http.get(`${endpoint}/sensor/heatmap/color`, {headers: this.headers}).toPromise();
  }

  
  
}
