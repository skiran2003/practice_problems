import java.util.LinkedList;

public class Example {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<>();
        list.add(15);
        list.add(30);
        list.addFirst(45); // Adding 45 at the beginning
        list.addLast(60);  // Adding 60 at the end
        list.add(2, 75); // Adding 75 at index 2

        System.out.println("List after additions: " + list);

        list.removeFirst(); // Removing the first element
        list.removeLast();  // Removing the last element
        list.remove(1); // Removing the element at index 1
        System.out.println("List after removals: " + list);

        System.out.println("First element: " + list.getFirst()); // Getting the first element
        System.out.println("Last element: " + list.getLast()); // Getting the last element
        System.out.println("Element at index 0: " + list.get(0)); // Getting the element at index 0

        System.out.println("Size of the list: " + list.size()); // Getting the size of the list
    }
}