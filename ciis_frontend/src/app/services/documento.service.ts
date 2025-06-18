// Ubicación: src/app/services/documento.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Documento {
  id: number;
  titulo: string;
  tipo_documento_display: string;
  autor_principal_username: string;
}

@Injectable({
  providedIn: 'root'
})
export class DocumentoService {
  private apiUrl = 'http://127.0.0.1:8000/ciis/api/documentos/';

  constructor(private http: HttpClient) { }

  getDocumentos(): Observable<Documento[]> {
    return this.http.get<Documento[]>(this.apiUrl);
  }
}
