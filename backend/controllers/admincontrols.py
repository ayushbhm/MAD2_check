from flask import Blueprint, jsonify,request
import base64
from models.models import BookDetails, BookCategory,BookRequests,BookRating,db

from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

admincontrols_bp = Blueprint('admincontrols', __name__, )



@admincontrols_bp.route('/api/admin_dashboard', methods=['GET'])
def admin_dashboard_api():
    # Query book details along with the user it is issued to (if approved), return date, and request date
    book_details = db.session.query(
        BookDetails.title,
        BookDetails.author,
        BookDetails.category,
        BookRequests.username,
        BookRequests.return_date,
        BookRequests.request_date
    ).join(
        BookRequests, BookDetails.id == BookRequests.book_id
    ).filter(
        BookRequests.status == 'approved'
    ).all()

    # Format book details as a list of dictionaries
    formatted_book_details = []
    for detail in book_details:
        formatted_book_details.append({
            'title': detail.title,
            'author': detail.author,
            'category': detail.category,
            'issued_to': detail.username,
            'return_date': str(detail.return_date),
            'request_date': str(detail.request_date)
        })

    # Return JSON response
    return jsonify(formatted_book_details)





@admincontrols_bp.route('/api/add_book_category', methods=['POST'])

def add_book_category():
    data = request.get_json()

    if not data or 'category' not in data:
        return jsonify({'error': 'Category data missing or invalid'}), 400

    category_name = data['category']

    # Check if the category already exists
    existing_category = BookCategory.query.filter_by(category=category_name).first()
    if existing_category:
        return jsonify({'error': 'Category already exists'}), 400

    try:
        # Create a new category
        new_category = BookCategory(category=category_name)
        db.session.add(new_category)
        db.session.commit()
        return jsonify({'message': 'Book category added successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while adding book category'}), 500
    finally:
        db.session.close()
        
        






@admincontrols_bp.route('/api//delete_book_category/<int:id>', methods=['DELETE'])

def delete_book_category(id):
    book_category = BookCategory.query.get(id)

    

    try:
        db.session.delete(book_category)
        db.session.commit()
        return jsonify({'message': 'Book category deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while deleting book category'}), 500
    finally:
        db.session.close()
        
        
        

@admincontrols_bp.route('/api/update_book_category/<int:id>', methods=['PUT'])

def update_book_category(id):
    data = request.get_json()

    if not data or 'category' not in data:
        return jsonify({'error': 'Category data missing or invalid'}), 400

    book_category = BookCategory.query.get(id)

    if not book_category:
        return jsonify({'error': 'Book category not found'}), 404

    try:
        # Update category data
        book_category.category = data['category']
        db.session.commit()
        return jsonify({'message': 'Book category updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while updating book category'}), 500
    finally:
        db.session.close()
