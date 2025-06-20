import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, tap } from 'rxjs';
import { MovieDetail, MovieResponse } from '../models/movie.model';
import { noImageBase64 } from '../models/no-image';

@Injectable({
  providedIn: 'root'
})
export class MovieService {
  private apiKey = '3fd2be6f0c70a2a598f084ddfb75487c'; // This is a public API key for demo purposes
  private baseUrl = 'https://api.themoviedb.org/3';

  constructor(private http: HttpClient) { }

  getPopularMovies(page: number = 1): Observable<MovieResponse> {
    return this.http.get<MovieResponse>(`${this.baseUrl}/movie/popular?api_key=${this.apiKey}&page=${page}`)
      .pipe(
        tap(response => console.log('Popular movies response:', response))
      );
  }

  getMovieDetails(id: number): Observable<MovieDetail> {
    console.log(`Fetching movie details for ID: ${id}`);
    return this.http.get<MovieDetail>(`${this.baseUrl}/movie/${id}?api_key=${this.apiKey}`)
      .pipe(
        tap(response => console.log('Movie details response:', response)),
        catchError(error => {
          console.error('Error fetching movie details:', error);
          throw error;
        })
      );
  }

  searchMovies(query: string, page: number = 1): Observable<MovieResponse> {
    return this.http.get<MovieResponse>(
      `${this.baseUrl}/search/movie?api_key=${this.apiKey}&query=${query}&page=${page}`
    ).pipe(
      tap(response => console.log('Search movies response:', response))
    );
  }

  getImageUrl(path: string, size: string = 'w500'): string {
    if (!path) {
      return noImageBase64;
    }
    return `https://image.tmdb.org/t/p/${size}${path}`;
  }
}
