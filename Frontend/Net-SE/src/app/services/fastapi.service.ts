

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class FastapiService {
  private apiUrl = 'http://192.168.120.87:8000/tab1'; 
  

  constructor(private http: HttpClient) {}

  obtenerSolucion(pregunta: string) {
    return this.http.get(`${this.apiUrl}/${pregunta}`);
  }
}
