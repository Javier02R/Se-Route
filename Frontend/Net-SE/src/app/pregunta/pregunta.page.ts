import { Component } from '@angular/core';
import { FastapiService } from '../services/fastapi.service';

@Component({
  selector: 'app-pregunta',
  templateUrl: 'pregunta.page.html',
  styleUrls: ['pregunta.page.scss'],
})
export class PreguntaPage {
  pregunta: string = '';
  solucion: string = '';

  constructor(private fastapiService: FastapiService) {}

  enviarPregunta() {
    this.fastapiService.obtenerSolucion(this.pregunta)
      .subscribe(
        (data: any) => {
          this.solucion = data.solucion;
        },
        (error) => {
          console.error('Error al obtener la solución', error);
        }
      );
  }
}
